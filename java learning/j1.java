class j1
{
    String name;int id;
j1()
{
    name="";
    id=0;
}
j1(int x,String nam)
{
    id=x;
    name=nam;
}
void display()
{
    System.out.println("The name is \n"+name+"the id is \n"+id);
}
    public static void main (String args[])

    {
        System.out.println("Showing exp1\n");
        j1 s1=new j1();
        j1 s2=new j1(10,"Sujit");
            s1.display();
            s2.display();
    }}
