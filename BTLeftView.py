from collections import deque
def BTLeftView(root):
    if not root:
        return

    q = deque()
    q.append(root)
    q.append(None)

    while (q):
        node = q.popleft()

        if node:
            print (node.val)

            while (q[0]):
                t = q[0]
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)

                q.pop(0)
            q.append(None)
        q.pop(0)