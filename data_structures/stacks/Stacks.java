/**
 * Implementation of a stack data structure of size n using an array of
 * size n as the underlying structure.
 * The stack has operations like stack-empty, push, and pop. And attributes
 * like S.top and S.size
 */

import java.util.EmptyStackException;

public class Stacks {

    private int[] stackElements = new int [20];
    private int size;
    private int top;

    public Stacks() {
        this.size = 0;
        this.top = 0;
    }

    public void push(int newValue) {
        if (this.top == this.size) {
            // Replace with error-handling logic later
            System.out.println("Overflow");
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

    public int pop() throws EmptyStackException {
        if (this.stackEmpty()) {
            throw new EmptyStackException();
        }
        this.top = this.top - 1;
        return this.stackElements[this.top + 1];
    }
}