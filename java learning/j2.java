class animal {
    void eat() {
        System.out.println("eat");
    }
}

class dog extends animal {
    void bark() {
        System.out.println("bark");
    }
}

class cat extends animal {
    void meow() {
        System.out.println("Meow itself");
    }
}

class puppy extends dog {
    void weeps() {
        System.out.println("Weeps");
    }
}

class j2 {
    public static void main(String args[]) {
        System.out.println("The Inheritance");
        dog d = new dog();
        puppy p = new puppy();
        cat c = new cat();

        System.out.println("\nSingle Inheritance");
        d.bark();
        d.eat();

        System.out.println("\nMultilevel Inheritance");
        p.weeps();
        p.eat();
        p.bark();

        System.out.println("\nHierarchical Inheritance");
        c.eat();
        c.meow();
    }
}
