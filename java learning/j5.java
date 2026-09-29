abstract class shape
{
 abstract void area();
 void show()
 {
     System.out.println("this is shape\n");
 }
}
class rectangle extends shape{
 void area()
 {
     System.out.println("the area of the rectangle is \n:"+(5*4));
 }
}
interface Animal
{
    void sound();

}
class dog implements Animal{
public  void sound()
{
    System.out.println("barking\n");
}
}
class j5
{
    public static void main(String args[])
    {
        System.out.println("Abstract class\n");
        rectangle s=new rectangle();
        s.show();
        s.area();
        System.out.println("the implement section");
        dog d=new dog();
        d.sound();

    }
}
