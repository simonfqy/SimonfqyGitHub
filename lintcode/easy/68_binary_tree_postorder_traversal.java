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
