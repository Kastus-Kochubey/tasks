package com.example.application_of_kastus_kochubey;

import android.graphics.Canvas;
import android.graphics.Paint;
import android.widget.Button;

public class MyView extends Button {
    float start_x, start_y, stop_x, stop_y;

    public MyView(float start_x, float start_y, float stop_x, float stop_y) {
        this.start_x = start_x;
        this.start_y = start_y;
        this.stop_x = stop_x;
        this.stop_y = stop_y;

    }

    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        Paint paint = new Paint:
        canvas.drawLine(start_x, start_y, stop_x, stop_y, paint);
    }
}
