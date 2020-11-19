package com.example.myapplication;

import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Point;

public class Circle extends Shape {
    String colorCircle;
    Point center;
    float radius;

    public Circle(String colorCircle, Point center, float radius){
        super(colorCircle);
        this.colorCircle = colorCircle;
        this.center = center;
        this.radius = radius;
    }

    void draw(Canvas canvas){
        if (center != null) {
            Paint paint = new Paint();
            paint.setColor(Color.parseColor(this.colorCircle));
            canvas.drawCircle(center.x, center.y, radius, paint);
        }
    }
}
