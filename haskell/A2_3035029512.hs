import Test.QuickCheck
import Data.Char
import Data.List
import Data.Maybe

-- Problem 1: Part I
-- To implement a function returning identical results as enumFromTo.
range :: Int -> Int -> [Int]
range x y =
    let diff = y - x --diff is the difference between two input integers.
    in take (diff+1) $ iterate (+1) x --take the first diff + 1 elements.

-- Problem 1: Part II
prop_range :: Int -> Int -> Bool
prop_range x y = enumFromTo x y == range x y

--Problem 2: Part I
-- calculate binomial coefficient. Because of the constraint of Int, we need to use
-- div to avoid compilation errors though the function never truly gets fractional numbers.
bi_coeff :: Int -> Int -> Int
bi_coeff n k
    | k == 0 = 1
    | otherwise = (n * bi_coeff (n-1) (k-1)) `div` k

--Problem 2: Part II
--To return a combination of elements, each combination with k elements.
--do notation ensures that the whole xs is examined. "y" and "body" is ensured
--to avoid duplications and the relative order of elements in each combination
--also strictly follow the initial input order of elements.
comb :: Int -> [a] -> [[a]]
comb 0 _  = [[]]
comb k xs
    | k == 0 = [[]]
    | otherwise = do
            (y:ys) <- tails xs
            body <- comb (k-1) ys
            return $ y:body

--Problem 2: Part III
prop_comb :: Int -> [a] -> Property
prop_comb k xs = (k >= 0 && length xs <= 20) ==> (length $ comb k xs) == bi_coeff n k
    where n = length xs

--Problem 3
--to implement an identifier which examines whether a string is legal. Here I use guards
--to return False whenever some illegal instances are observed.
identifier :: String -> Bool
identifier xs
    | not $ all (`elem` (['a'..'z'] `union` ['A'..'Z'] `union` ['-'] `union` ['0'..'9'])) xs = False
    | (head $ reverse xs) == '-' = False
    | (head xs) `elem` (['-'] `union` ['0'..'9']) = False
    | length xs == 1 = True
    | otherwise = not $ checkHyphen xs
            where checkHyphen [] = False
                  checkHyphen ('-':'-':ys) = True
                  checkHyphen (y:ys) = False || (checkHyphen ys)

-- Problem 4: Part I
-- In order to facilitate the foldr implementation in function toTree, an additional
-- helper function treeInsert is created, which is used for inserting an element into
-- the binary tree and update the height fields.
data Tree a = Leaf | Node Int (Tree a) a (Tree a)
              deriving (Eq, Show)
height :: Tree a -> Int
height Leaf = 0
height (Node h left a right) = max (height right) (height left) + 1

treeInsert :: a -> Tree a -> Tree a
treeInsert x Leaf = Node 1 Leaf x Leaf
treeInsert x (Node h left a right) -- h is only for holding place. No use.
    | (height left) >= (height right) = let hnew = height (Node h left a (treeInsert x right))
                                    in Node hnew left a (treeInsert x right)
    | (height right) > (height left) = let hnew = height (Node h (treeInsert x left) a right)
                                    in Node hnew (treeInsert x left) a right

toTree :: [a] -> Tree a
toTree xs = foldr treeInsert Leaf xs

-- Problem 4: Part II
-- In the "where" helper function getLeft and getRight, function height as defined before
-- are used.
prop_toTree :: [a] -> Bool
prop_toTree xs = let tree = toTree xs in (abs $ (getLeft tree) - (getRight tree)) < 2
    where getLeft (Node h left a right) = height left
          getLeft Leaf = -1
          getRight (Node h left a right) = height right
          getRight Leaf = -1

-- Problem 5: Part I
-- To get the width of a circuit and return Nothing if invalid, Just x if valid, where
-- x is the width of the circuit.
-- We incorporated a helper function getValue to get the value of a Maybe Int object.
-- getValue Nothing will never be encountered, put here to avoid compilation error.
type Size = Int --positive
data Circuit = Identity Size |
               Fan Size |
               Above Circuit Circuit |
               Beside Circuit Circuit |
               Stretch [Size] Circuit
               deriving (Show)
getValue :: Maybe Int -> Int
getValue (Just s) = s
getValue Nothing = 0

width :: Circuit -> Maybe Int
width (Identity s) = Just s
width (Fan s) = Just s
width (Beside c1 c2)
    | (width c1 /= Nothing) && (width c2 /= Nothing) = Just (
            (getValue $ width c1 ) + (getValue $ width c2))
    | otherwise = Nothing
width (Above c1 c2)
    | (width c1 /= Nothing) && (width c2 == width c1) = width c1
    | otherwise = Nothing
width (Stretch ws c)
    | (length ws) == (getValue $ width c) = Just $ sum ws
    | otherwise = Nothing

-- Problem 5: Part II
-- eval function evaluates the output of a circuit.
-- To make it valid, we return empty list when illegal circumstances are encountered,
-- like when size <= 0 or width function returns "Nothing".
-- The Stretch constructor requires some complicated maneuvers to evaluate its output.

eval :: Circuit -> [[Int]]
eval (Identity s)
    | s <= 0 = []
    | otherwise = eval (Identity (s-1)) ++ [[s]]
eval (Fan s)
    | s <= 0 = []
    | s == 1 = [[1]]
    | otherwise = eval (Fan (s-1)) ++ [[1, s]]
eval (Beside c1 c2)
    | width (Beside c1 c2) == Nothing = []
    | otherwise = (eval c1) ++ map (map (+w)) (eval c2)
        where w = getValue $ width c1
eval (Above c1 c2)
    | width (Above c1 c2) == Nothing = []
    | otherwise = map sort $ zipWith union (eval c1) (eval c2)
eval (Stretch ws c)
    | width (Stretch ws c) == Nothing = []
    | otherwise = let c2 = switchIndex (eval c) pos
                      c1 = eval (Identity (sum ws))
                  in  listFiller pos c1 c2
         where pos = tail $ scanl (+) 0 ws --gives the position of special circuit wires.

--Below are helper functions.
--switchHelper is the most basic helper function. It takes a list containing indices
--and a list with corresponding values. For example, c1 = [1, 2], c2 = [3, 5, 8].
--Then switchHelper c1 c2 = [3, 5]. If c1 = [1, 3], then switchHelper c1 c2 = [3, 8].
switchHelper :: [Int] -> [Int] -> [Int]
switchHelper [] val = []
switchHelper (x:ys) val = (val!!(x-1)) : (switchHelper ys val)

--switchIndex makes use of switchHelper, and converts a list of list of indices into
--a list of list of values. For example, switchIndex [[1], [1, 2], [1, 3]] [3, 5, 8]
-- = [[3], [3, 5], [3,8]]
switchIndex :: [[Int]] -> [Int] -> [[Int]]
switchIndex [] val = []
switchIndex (xs : xss) val = [switchHelper xs val] ++ (switchIndex xss val)

--listFilter is the final function used to transform an identity circuit output into
--a Stretch circuit output. The first list argument provides the indices in the identity
--circuit output that should be replaced by the corresponding entry (also a list) in c2,
--and c1 is simply the identity circuit output to work on. For example, listFiller [3,5,8]
--(eval (Identity 8)) [[3], [3, 5], [3, 8]] will have [3], [3, 5] and [3, 8] at its third,
--fifth and eighth entries, while other entries remain the same as an identity circuit.
listFiller :: [Int] -> [[Int]] -> [[Int]] -> [[Int]]
listFiller [] c1 c2 = c1
listFiller (x:xs) c1 (ys:yss) = let earlier = take (x-1) c1
                                    later = drop x c1
                                in  listFiller xs (earlier ++ [ys] ++ later) yss

