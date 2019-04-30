/**
* 本参考程序来自九章算法，由 @Y同学 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code

preorder, inorder, postorder通用非递归解法：记录每个点是否是第二次出栈。就是要额外费点存储空间
*/ 

public List<Integer> postorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        Set<TreeNode> checkedSet = new HashSet<TreeNode>();
        
        List<Integer> list = new ArrayList<Integer>();
        if(root!=null) {
            stack.push(root);
        }
        
        while(!stack.isEmpty()) {
            TreeNode top = stack.pop();
            if(checkedSet.contains(top)) {
                list.add(top.val);
            }
            else {
                //postorder
                stack.push(top);
                checkedSet.add(top);
                if(top.right!=null) {
                    stack.push(top.right);
                }
                if(top.left!=null) {
                    stack.push(top.left);
                }
                
                //inorder
                /*
                if(top.right!=null) {
                    stack.push(top.right);
                }
                stack.push(top);
                checkedSet.add(top);
                if(top.left!=null) {
                    stack.push(top.left);
                }
                */
                
                //preorder
                /*
                if(top.right!=null) {
                    stack.push(top.right);
                }
                if(top.left!=null) {
                    stack.push(top.left);
                }
                stack.push(top);
                checkedSet.add(top);
                */
            }
        }
        
        return list;
    }


// The following solution is conceptually similar to the last one.
/**
* 本参考程序来自九章算法，由 @Z同学 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/ 

public class Solution {
    
    public enum Operation {
        RPOCESS, 
        ADDTORESULT
    }
    
    /**
     * @param root: A Tree
     * @return: Postorder in ArrayList which contains node values.
     */
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        
        if (root == null) {
            return result;
        }
        
        Stack<TreeNode> stack = new Stack<>();
        Stack<Operation> operationStack = new Stack<>();
        
        stack.push(root);
        operationStack.push(Operation.RPOCESS);
        
        while (!stack.empty()) {
            TreeNode node = stack.pop();
            Operation operation = operationStack.pop();
            
            if (node == null) {
                continue;
            }
            
            if (operation == Operation.ADDTORESULT) {
                result.add(node.val);
            }
            else {
                stack.push(node);
                operationStack.push(Operation.ADDTORESULT);
                
                stack.push(node.right);
                operationStack.push(Operation.RPOCESS);
                
                stack.push(node.left);
                operationStack.push(Operation.RPOCESS);
            }
        }
        
        return result;
    }
}


// 官方解法
/**
* 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/ 

//Recursive
public ArrayList<Integer> postorderTraversal(TreeNode root) {
    ArrayList<Integer> result = new ArrayList<Integer>();

    if (root == null) {
        return result;
    }

    result.addAll(postorderTraversal(root.left));
    result.addAll(postorderTraversal(root.right));
    result.add(root.val);

    return result;   
}

//Iterative
// 使用栈进行二叉树后序遍历，首先对左子树进行遍历压入栈中，直至左子树为空，然后访问右子树。
// 故每个节点会被访问两次，当节点被第二次访问时，该节点出栈。
public ArrayList<Integer> postorderTraversal(TreeNode root) {
    ArrayList<Integer> result = new ArrayList<Integer>();
    Stack<TreeNode> stack = new Stack<TreeNode>();
    TreeNode prev = null; // previously traversed node
    TreeNode curr = root;

    if (root == null) {
        return result;
    }

    stack.push(root);
    while (!stack.empty()) {
        curr = stack.peek();
        if (prev == null || prev.left == curr || prev.right == curr) { // traverse down the tree
            if (curr.left != null) {
                stack.push(curr.left);
            } else if (curr.right != null) {
                stack.push(curr.right);
            }
        } else if (curr.left == prev) { // traverse up the tree from the left
            if (curr.right != null) {
                stack.push(curr.right);
            }
        } else { // traverse up the tree from the right
            result.add(curr.val);
            stack.pop();
        }
        prev = curr;
    }

    return result;
}
