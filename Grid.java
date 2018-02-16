package mr;
class Grid 
{	
	public static  int x=1;
    public static  int y=1;
    public static  String d="north";
    String[] dir= {"north","east","south","west"};
    int flag=0;
    int check_bound()
	{
		if(x==1&& d=="north"|| y==3 && d=="east"||x==3 && d=="east"||y==1 && d=="west")
			return 0;
		return 1;
	}
    public static void main(String args[])
    {
    	robot r=new robot();
    	r.move();
    	r.rotate();
    	r.rotate();
    	r.move();
    	r.move();
    	r.rotate();
    	r.rotate();
    	System.out.println("the robot is at "+x+","+y+"and facing towards"+d);
    }
    
}
class robot extends Grid
{
	Grid g=new Grid();
    void move()
    {
		if(g.check_bound()!=0)
		{
			if(d=="north"||d=="south")
				x++;
			else
				y++;
		}	
    }
    void rotate()
    {
    	int i;
    	int index;
		for( i=0;i<3;i++)
		{
			if (d==dir[i])
			{
				index=i+1;
				d=dir[index];
				break;
			}
			if(d==dir[3])
			{
				d=dir[0];
				break;
			}
		}		
    }   
}


