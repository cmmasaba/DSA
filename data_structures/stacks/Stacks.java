/**
 * Implementation of a stack data structure of size n using an array of
 * size n as the underlying structure.
 * The stack has operations like stack-empty, push, and pop. And attributes
 * like S.top and S.size
 */

public class Stacks {

    private int[] stackElements = new int [20];
    private int size;
    private int top;

    public Stacks() {
        this.size = 20;
        this.top = 0;
    }

    public void push(int newValue) throws StackExceptions {
        if (this.top == this.size) {
            throw new StackExceptions("Stack overflow!!!");
        } else {
            this.top = this.top + 1;
            this.stackElements[this.top] = newValue;
        }
    }

    public boolean stackEmpty() {
        if (this.top == 0) {
            return true;
        } else {
            return false;
        }
    }

    public int pop() throws StackExceptions {
        if (this.stackEmpty()) {
            throw new StackExceptions("Stack Underflow!!!");
        }
        this.top = this.top - 1;
        return this.stackElements[this.top + 1];
    }
}