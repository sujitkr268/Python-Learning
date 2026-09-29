class j7 {
    public static void main(String args[]) {

        // String methods
        System.out.println("String Methods");
        String s = "Hello Java";
        System.out.println("String = " + s);
        System.out.println("Length = " + s.length());
        System.out.println("Uppercase = " + s.toUpperCase());
        System.out.println("Lowercase = " + s.toLowerCase());
        System.out.println("Character at index 1 = " + s.charAt(1));
        System.out.println("Substring(6) = " + s.substring(6));
        System.out.println("Replace a with o = " + s.replace('a', 'o'));
        System.out.println("Index of J = " + s.indexOf('J'));
        System.out.println("Equals Hello Java? " + s.equals("Hello Java"));
        System.out.println("Concat = " + s.concat(" World"));

        // StringBuffer methods
        System.out.println("\nStringBuffer Methods");
        StringBuffer sb = new StringBuffer("Hello");
        sb.append(" Java");
        System.out.println("After append = " + sb);
        sb.insert(5, ",");
        System.out.println("After insert = " + sb);
        sb.replace(0, 5, "Hi");
        System.out.println("After replace = " + sb);
        sb.delete(2, 3);
        System.out.println("After delete = " + sb);
        sb.reverse();
        System.out.println("After reverse = " + sb);
    }
}
