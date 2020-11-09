package com.example.application_submarinegame;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;

import static android.content.ContentValues.TAG;

public class CustomView extends View {
    int cellsSize = 40;
    int numberHorCells = getWidth() / cellsSize;
    int numberVertCells = getHeight() / cellsSize;
    float density;
    float vertCellSize;
    float horCellSize;

    public CustomView(Context context) {
        super(context);
    }

    public CustomView(Context context, float density) {
        super(context);
        this.density = density;
    }

//    public CustomView(int numberHorCells, int numberVertCells) {
//        this.numberHorCells = numberHorCells;
//        this.numberVertCells = numberVertCells;
//
//    }


    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        numberHorCells = (getWidth() % cellsSize == 0) ? getWidth() / cellsSize - 1 : getWidth() / cellsSize;
        numberVertCells = (getHeight() % cellsSize == 0) ? getHeight() / cellsSize - 1 : getHeight() / cellsSize;
        vertCellSize = (float) getHeight() / numberVertCells;
        horCellSize = (float) getWidth() / numberHorCells;
        Paint paint = new Paint();
        paint.setStrokeWidth(density);

        for (int x = 0; x < numberVertCells; x++) {
            canvas.drawLine(x * horCellSize, 0, x * horCellSize, getHeight(), paint);

        }
        for (int y = 0; y < numberVertCells + 1; y++) {
            canvas.drawLine(0, y * vertCellSize, getWidth(), y * vertCellSize, paint);
        }
    }



    @Override
    public boolean onTouchEvent(MotionEvent event) {
        Log.d(TAG, String.format("onTouchEvent: X: %f Y:%f", event.getX(), event.getY()));

        return super.onTouchEvent(event);
    }
}
