from animal import dog # animal 패키지에서 dog 라는 모듈을 갖고와줘
from animal import cat # animal 패키지에서 cat 라는 모듈을 갖고 와줘
from animal import * # animal 패키지가 갖고 있는 모듈을 다 불러봐

d = Dog()
c = Cat()

d.hi()
c.hi()