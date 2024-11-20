/**
 * Implementation of a Queue data structure of size n-1 using
 * an array of size n as the underlying structure.
 * The queue has operations like queue-empty, queue-full, enqueue and dequeue.
 * And attributes like Q.tail, Q.size and Q.head.
 */

package data_structures.queues;

public class Queue{
    private int[] queueElements = new int[20];
    private int size;
    private int tail;
    private int head;

    public Queue() {
        this.size = 20;
        this.tail = 0;
        this.head = 0;
    }

    public boolean isQueueEmpty() {
        if (this.head == this.tail) {
            return true;
        } else {
            return false;
        }
    }

    public boolean isQueueFull() {
        if ((this.head == this.tail + 1) || (this.head == 1 && this.tail == this.size)) {
            return true;
        } else {
            return false;
        }
    }

    public void enqueue(int newValue) throws QueueExceptions {
        if (!isQueueFull()) {
            this.queueElements[this.tail] = newValue;
            if (this.tail == this.size - 1) {
                this.tail = 0;
            } else {
                this.tail = this.tail + 1;
            }
        } else {
            throw new QueueExceptions("Queue overflow!!!");
        }
    }

    public int dequeue() throws QueueExceptions {
        if (!isQueueEmpty()) {
            int value = this.queueElements[this.head];
            if (this.head == this.size - 1) {
                this.head = 0;
            } else {
                this.head = this.head + 1;
            }
            return value;
        } else {
            throw new QueueExceptions("Queue underflow!!!");
        }
    }
}