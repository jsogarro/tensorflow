"""SimpleFlow Classification

A simple script that demonstrates how to use a simple TensforFlow implementation to classify data.
"""
import simpleflow.main as sf


def main():
    g = sf.Graph()
    g.initialize_globals()

    # create our placeholders, variables and define our activation function
    X = sf.Placeholder()
    W = sf.Variable([1,1])
    b = sf.Variable(-5)
    z = sf.add(sf.matmul(W, X), b)
    a = sf.Sigmoid(z)

    # create the session and run it
    sess = sf.Session()
    result = sess.run(operation=a, feed_dict={X:[8,10]})
    print(result)

if __name__ == '__main__':
    main()
