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
    boolean doDrawHit;
    float posX;
    float posY;

    {
        Log.i("CustomView", getWidth() + "");
    }


    public CustomView(Context context) {
        super(context);
    }

    public CustomView(Context context, float density) {
        super(context);
        this.density = density;
//        Log.i("CustomView", numberHorCells + ", " + numberVertCells);

    }

//    public CustomView(int numberHorCells, int numberVertCells) {
//        this.numberHorCells = numberHorCells;
//        this.numberVertCells = numberVertCells;
//
//    }


    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);

        Log.i("CustomView", getWidth() + "");
        numberHorCells = getWidth() / cellsSize;
        numberVertCells = getHeight() / cellsSize;
        vertCellSize = (float) getHeight() / numberVertCells;
        horCellSize = (float) getWidth() / numberHorCells;
        Paint paint = new Paint();
        paint.setStrokeWidth(this.density * 2.2f);

        for (int x = 0; x < numberVertCells; x++) {
            canvas.drawLine(x * horCellSize, 0, x * horCellSize, getHeight(), paint);

        }
        for (int y = 0; y < numberVertCells + 1; y++) {
            canvas.drawLine(0, y * vertCellSize, getWidth(), y * vertCellSize, paint);
        }

        drawHit(canvas);
//        canvas.drawLine(10, 0, 10, 1000, paint);
    }

    private void drawHit(Canvas canvas) {
         Paint paint = new Paint();
         paint.setStrokeWidth(10);
         paint.setColor(222222);

        if (doDrawHit) {
            canvas.drawCircle(posX, posY, 50, paint);
        } else {
            canvas.drawLine(10, 0, 10, 1000, paint);
        }
    }

    public void hit() {

    }

    public boolean gotAHit(float x, float y) {

        if (x - MainActivity.cellX * horCellSize < 40 &&
                y - MainActivity.cellY * vertCellSize < 40 &&
                x - MainActivity.cellX * horCellSize > 0 &&
                y - MainActivity.cellY * vertCellSize > 0) {
            return true;
        }
        return false;
    }
    @Override
    public boolean onTouchEvent(MotionEvent event) {
        Log.d(TAG, String.format("onTouchEvent: X: %f Y:%f", event.getX(), event.getY()));
        if (gotAHit(event.getX(), event.getY())) {
            doDrawHit = true;
        } else {
            posX = event.getX();
            posY = event.getY();
        }

        invalidate();
        return super.onTouchEvent(event);
    }
}
