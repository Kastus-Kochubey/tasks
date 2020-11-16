package com.example.myapplication;

import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Point;

public class Rectangle {
    String colorRect;
    Point corner;
    int widthRect;
    int heightRect;

    public Rectangle(String colorRect, Point corner, int widthRect, int heightRect){
        this.colorRect = colorRect;
        this.corner = corner;
        this.widthRect = widthRect;
        this.heightRect = heightRect;
    }

    void draw(Canvas canvas){
        if (corner != null) {
            Paint paint = new Paint();
            paint.setColor(Color.parseColor(this.colorRect));
            canvas.drawRect(corner.x, corner.y, corner.x + widthRect, corner.y + heightRect, paint);
        }
    }
}
