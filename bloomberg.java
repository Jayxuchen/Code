//check if a string is a palindrome

public class PathFinder{
  dirX;
  dirY;
  Point start;
  Point end;
  List <Queue<Point>> pathList;
  public PathFinder(Point start, Point end)
  {
    this.start = start;
    this.end = end;
    //finds direction of unit vector between start and end point
    //for X axis
    if(start.getX()-end.getX() < 0){
      dirX=-1;
    }
    else if(start.getX()-end.getX() > 0{
      dirX=1;
    }
    else{
      dirX = 0;
    }
    //for Y axis.
    if(start.getY()-end.getY() < 0){
      dirY=-1;
    }
    else if(start.getY()-end.getY() > 0{
      dirY=1;
    }
    else{
      dirY = 0;
    }
    if(dirX == 0  && dirY == 0){
      System.out.println("error: start and end points are the same");
      return;
    }
    Queue<Point> initialList = new Queue<Point>();
    recursiveSearch(initialList,this.start);
  }
  public List<Queue<Point>> getPaths()
  {
    return pathList;
  }
  public void addPath(List<Point> newList){
    pathList.insert(newList);
  }
  public void recursiveSearch(Queue<Point> pointList,Point thePoint)
  {
    if(isValid(thePoint))
    {
      Queue<Point> p = pointList;
      p.insert(thePoint);
      if(thePoint.getX()==end.get(x) && thePoint.getY() = end.getY())
      {
        addPath(p);
        return;
      }
      else{
        Point pointIncX = new Point(thePoint.getX()+dirX,thePoint.getY());
        recursiveSearch(p,pointIncX);
        Point pointIncY = new Point(thePoint.getX(),thePoint.getY()+dirY);
        recursiveSearch(p,pointIncY);
      }
    }
    return;
  }
  public boolean isValid(Point){
    if((Point.getX() > start.getX() && Point.getX()<end.getX())||
      (Point.getX() < start.getX() && Point.getX() > end.getX())
    {
      if((Point.getY() > start.getY() && Point.getY()<end.getY())||
        (Point.getY() < start.getY() && Point.getY() > end.getY())
          return true;
    }
    return false;
  }
}