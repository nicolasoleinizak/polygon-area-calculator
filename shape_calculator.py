class Rectangle:

  def __init__(self, width, height) -> None:
    self.width = width
    self.height = height
    pass
  
  def set_width (self, width):
    self.width = width

  def set_height (self, height):
    self.height = height

  def get_area (self):
    return self.width * self.height

  def get_perimeter (self):
    return 2 * self.width + 2 * self.height
  
  def get_diagonal (self):
    return (self.width ** 2 + self.height ** 2) ** 0.5
  
  def get_picture (self):
    if(self.width > 50 or self.height > 50):
      return "Too big for picture."
    picture = ''
    line = "".center(self.width, "*")
    for i in range(self.height):
      picture += line + "\n"
    return picture
  
  def get_amount_inside (self, shape):
    fits_horizontal = self.width // shape.width
    fits_vertical = self.height // shape.height
    return fits_horizontal * fits_vertical
  
  def __str__(self) -> str:
    return "Rectangle(width={}, height={})".format(self.width, self.height)
class Square (Rectangle):
  def __init__(self, width) -> None:
    super().__init__(width, width)

  def set_side (self, length):
    self.width = length
    self.height = length

  def set_height(self, height):
    self.width = height
    self.height = height
  
  def set_width(self, width):
    self.width = width
    self.height = width

  def __str__(self) -> str:
    return "Square(side={})".format(self.height)