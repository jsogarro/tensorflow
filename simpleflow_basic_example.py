"""SimpleFlow Script

A simple script that demonstrates how to use a simple TensforFlow implementation written by hand.
"""
import simpleflow.main as sf

def main():
    g = sf.Graph()
    g.initialize_globals()

    # create our placeholders, variables and define our activation function
    A = sf.Variable([[10,20], [30,40]])
    b = sf.Variable([1,2])
    x = sf.Placeholder()
    y = sf.matmul(A, x)
    z = sf.add(y, b)

    # create the session
    sess = sf.Session()
    result = sess.run(operation=z, feed_dict={x:10})
    print(result)

if __name__ == '__main__':
    main()
