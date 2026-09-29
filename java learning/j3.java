class  cal
{
    void add()
    {
        System.out.println("");
    }
   int add(int x,int y,int z)
    {
        return (x+y+z);
    }
    int add(int x,int y)
    {
        return (x+y);
    }
}
class shape
{
    void dis()
    {
        System.out.println("the shape are as follow\n");
    }
}
class square extends shape{
    void display()
    {
        System.out.println("its sqaure\n");
    }
}
class j3
{
    public static void main(String args[])
        {
            System.out.println("Method overloading\n");
            cal c=new cal();
           int k1= c.add(1,2);
            int k2=c.add(1,1,1);
        System.out.println(k1+""+k2);
        System.out.println("the method overriding\n");
        shape s=new shape();
        s.dis();
        square s1=new square();
        s1.display();
        s1.dis();


    }
}
