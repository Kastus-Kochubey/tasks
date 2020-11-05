package com.example.application_submarinegame;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.view.View;

public class CustomView extends View {
    int numberHorCells = getWidth() / 30;
    int numberVertCells = getHeight() / 30;

    public CustomView(Context context) {
        super(context);
    }

    public CustomView(Context context) {
        super(context);
        this.density =
    }

//    public CustomView(int numberHorCells, int numberVertCells) {
//        this.numberHorCells = numberHorCells;
//        this.numberVertCells = numberVertCells;
//
//    }


    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        numberHorCells = (getWidth() % 30 == 0) ? getWidth() / 30 - 1 : getWidth() / 30;
        numberVertCells = (getHeight() % 30 == 0) ? getHeight() / 30 - 1 : getHeight() / 30;
        Paint paint = new Paint();
        paint.setStrokeWidth(density);

        for (int x = 0; x < numberVertCells; x++) {
            canvas.drawLine(x * 30, 0, x * 30, getWidth(), paint);

        }
        for (int y = 0; y < numberVertCells - 1; y++) {
            canvas.drawLine(0, y * 30, 0, getHeight(), paint);

        }
    }
}
