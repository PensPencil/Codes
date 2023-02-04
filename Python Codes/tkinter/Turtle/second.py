from turtle import *

from sklearn.metrics import davies_bouldin_score
color('red','yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done