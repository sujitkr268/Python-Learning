
import java.util.*;
import java.io.*;
class j6
{
public static void main(String args[])throws IOException
{
    System.out.println("BufferReader\n");
    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    System.out.println("enter you city name\n");
    String str=br.readLine();
    System.out.println("City="+str);
    System.out.println("\nScanner");
           System.out.print("Enter your name and age (example: Sujit 20): ");
           Scanner sc = new Scanner(br.readLine());
           String name = sc.next();
           int age = sc.nextInt();
           System.out.println("Name = " + name + ", Age = " + age);
}
}
