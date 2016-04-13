module A1_3035029512 where
import Test.QuickCheck

-- Problem 1: Part I
gcd' :: Int -> Int -> Int
gcd' a b
    | b == 0 = a
    | otherwise = gcd' b c
    where c = mod a b
{-gcd' a 0 = a
gcd' a b = gcd' b (a `mod` b) -}

-- Problem 1: Part II
prop_gcd :: Int -> Int -> Property
prop_gcd a b = (a >= 0 && b >= 0) ==> (gcd a b) == (gcd' a b)

{- Problem 2: Part I
insert :: Int -> [Int] -> [Int]
insert a [] = [a]
insert a (x:xs) = x:(insert a xs)

-- Problem 2: Part II
insertsort :: [Int] -> [Int]
insertsort [] = []
insertsort (x:xs) =
    let smallersorted = insertsort[a|a <- xs, a <=x ]
        biggersorted = insertsort[a|a <- xs, a > x]
    in  (insert x smallersorted) ++ biggersorted -}

-- Problem 2: Part I
insert :: Int -> [Int] -> [Int]
insert x [] = [x]
insert y (x:xs) = if x < y then x:y:ys else y:insert x ys

-- Problem 2: Part II
insertsort :: [Int] -> [Int]
insertsort [] = []
insertsort (x:xs) = insert x (insertsort xs)

{-- Problem 3
sieve :: [Int] -> [Int]
sieve [] = []
sieve (x:xs) = x:(sieve [a| a <- xs, a `mod` x /= 0])

sievePrime :: Int -> [Int]
sievePrime x = sieve [2..x] -}

sieve :: [Int] -> [Int]
sieve [] = []
sieve (x:xs) = x: sieve(filter (\n -> n `mod` x /=0) xs)

sievePrime :: Int -> [Int]
sievePrime x = sieve[2..x]

-- Problem 4: Part I
next :: Int -> Int
next a
    | even a = quot a 2
    | odd a = 3*a+1

-- Problem 4: Part II
terminate :: Int -> Bool
terminate a
    | a == 1 = True
    | otherwise = terminate $ next a

-- Problem 4: Part III
terminate' :: Int -> Int -> Bool
terminate' n i
    | (n == 1 && i <= 500) = True
    | i > 500 = False
    | otherwise = terminate' (next n) (i+1)

-- Problem 4: Part IV
prop_terminate :: Int -> Property
prop_terminate n =  (n <= 10000 && n > 0) ==> terminate' n 0 == True

-- Problem 4: Part V
numSteps :: Int -> [Int]
numSteps n = zipWith (\n i -> terminate'' n i) [1..n] (replicate n 0)
  where terminate'' n i
            | n == 1 = i
            | otherwise = 1 + terminate'' (next n) i



