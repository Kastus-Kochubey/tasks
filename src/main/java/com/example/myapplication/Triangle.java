package com.example.myapplication;

import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Path;
import android.graphics.Point;

public class Triangle extends Shape{
    String colorTriangle;
    Point a = null;
    Point b = null;
    Point c = null;



    public Triangle(String colorTriangle, Point a, Point b, Point c){
        super(colorTriangle);
        this.colorTriangle = colorTriangle;
        this.a = a;
        this.b = b;
        this.c = c;
    }

    void draw(Canvas canvas){
        if (a != null) {
            Paint paint = new Paint();
            paint.setColor(Color.parseColor(this.colorTriangle));
            Path path = new Path();
            path.moveTo(a.x, a.y);
            path.lineTo(b.x, b.y);
            path.lineTo(c.x, c.y);
            path.lineTo(a.x, a.y);

            canvas.drawPath(path, paint);
        }
    }
}
