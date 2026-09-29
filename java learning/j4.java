class account
{
    private int id;private double balanc;
    void setacc(int x)
    {
       id=x;
    }
    void setbal(double y)
    {
      balanc=y;
    }
    double getacc()
    {
        return id;
    }

    double getbalan()
    {
        if( balanc>0)
        {
        return balanc;
        }
        else{
            return 0;
        }
    }
}
class j4
{
    public static void main(String args[])
    {
        System.out.println("Encapsulation\n");
        account a=new account();
        a.setacc(120);
      System.out.println("the account number is\n"+a.getacc());
      a.setbal(12000);
      System.out.println("the balance is \n"+a.getbalan());
    }
}
