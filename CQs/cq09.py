class Line:
    start: Point
    end: Point

    def __init__(self, start: Point, end: Point):
        self.start=start
        self.end=end

    def get_length(self) -> float:
        #calculates the length of the line
        x_diffs:float=self.end.x-self.start.x
        y_diffs:float=self.end.y-self.start.y
        return (x_diffs**2+y_diffs**2)**0.5

    def get_slope(self) -> float: 
        #calculates the slope (from start to end)
        Rise:float=self.end.y-self.start.y
        Run:float=self.end.x-self.start.x
        return Rise/Run