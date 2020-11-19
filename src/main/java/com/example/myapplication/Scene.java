package com.example.myapplication;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.DashPathEffect;
import android.graphics.Paint;
import android.graphics.Path;
import android.graphics.Point;
import android.util.AttributeSet;
import android.view.MotionEvent;
import android.view.View;

import androidx.annotation.Nullable;

public class Scene extends View {
    Point[] points = new Point[3];
    float density;
    int gridSize = 30;
    int gridWidth;
    int gridHeight;
    int countPoints;
    String mode = "draw";
    String typeShape = "rect";
    String color = "#000000";

    // свойства прямоугольника
//    int rectCount;
//    Rectangle[] rectangles = new Rectangle[33];
//
//
//    // свойства круга
//    int circleCount;
//    Circle[] circles = new Circle[33];
//
//
//
//
//    // свойства треугольника
//    int triangleCount;
//    Triangle[] triangles = new Triangle[33];

    int shapesCount;
    Shape[] shapes = new Shape[100];




    public Scene(Context context, @Nullable AttributeSet attrs) {
        super(context, attrs);
        density = getResources().getDisplayMetrics().density;
        gridSize *= density;
    }

    private void createRect(String color, Point corner, int width, int height) {
        shapes[shapesCount] = new Rectangle(color, corner, width, height);
        shapesCount += 1;

//        this.colorRect = color;
//        this.corner = corner;
//        this.widthRect = width;
//        this.heightRect = height;
    }

    private void createCircle(String color, Point center, float radius) {
        shapes[shapesCount] = new Circle(color, center, radius);
        shapesCount += 1;
    }

    private void createTriangle(String color, Point a, Point b, Point c) {
        shapes[shapesCount] = new Triangle(color, a, b, c);
        shapesCount += 1;
    }

    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        gridWidth = getWidth() / gridSize;
        gridHeight = getHeight() / gridSize;

        drawGrid(canvas);
        drawPoints(canvas);

        drawShapes(canvas);
//        drawRectangles(canvas);
//        drawCircle(canvas);
//        drawTriangle(canvas);
    }


    private void drawShapes(Canvas canvas){
        for (int i = 0; i < shapesCount; i++) {
            shapes[i].draw(canvas);
        }
    }

//    private void drawTriangle(Canvas canvas) {
//        if (a != null) {
//            Paint paint = new Paint();
//            paint.setColor(Color.parseColor(this.colorTriangle));
//
//            Path path = new Path();
//            path.moveTo(a.x, a.y);
//            path.lineTo(b.x, b.y);
//            path.lineTo(c.x, c.y);
//            path.lineTo(a.x, a.y);
//
//            canvas.drawPath(path, paint);
//        }
//    }

//    private void drawCircle(Canvas canvas) {
//        if (center != null) {
//            Paint paint = new Paint();
//            paint.setColor(Color.parseColor(this.colorCircle));
//            canvas.drawCircle(center.x, center.y, radius, paint);
//        }
//    }

//    private void drawRect(Canvas canvas) {
//        if (this.rect != null) {
//            this.rect.draw(canvas);
//        }
//    }

//    public void drawRectangles(Canvas canvas) {
//        for (int i = 0; i < rectCount; i++) {
//            Rectangle r = rectangles[i];
//            r.draw(canvas);
//        }
//    }

    private void drawGrid(Canvas canvas) {
        Paint paint = new Paint();
        paint.setStyle(Paint.Style.STROKE);
        DashPathEffect effects = new DashPathEffect(new float[]{3, 9}, 0);
        paint.setPathEffect(effects);

        for (int i = 0; i < gridWidth; i++) {
            int x = i * gridSize;
            canvas.drawLine(x, 0, x, getHeight(), paint);
        }

        for (int i = 0; i < gridHeight; i++) {
            int y = i * gridSize;
            int endX = getWidth();
            canvas.drawLine(0, y, endX, y, paint);
        }

    }

    private void drawPoints(Canvas canvas) {
        Paint paint = new Paint();
        paint.setColor(Color.RED);

        for (int i = 0; i < countPoints; i++) {
            Point point = points[i];
            canvas.drawCircle(point.x, point.y, 10, paint);
        }
    }

    @Override
    public boolean onTouchEvent(MotionEvent event) {
        if (event.getAction() == MotionEvent.ACTION_DOWN) {
            onDownTouch((int) event.getX(), (int) event.getY());
        }
        return true;
    }

    private void onDownTouch(int x, int y) {
        if (this.mode.equals("draw")) {
            points[countPoints] = new Point(x, y);
            countPoints += 1;

            switch (this.typeShape) {
                case "rect":
                    checkRectForCreating();
                    break;
                case "circle":
                    checkCircleForCreating();
                    break;
                case "triangle":
                    checkTriangleForCreating();
                    break;
            }

            invalidate();
        }
    }

    private void checkRectForCreating() {
        if (countPoints >= 2) {
            int width = points[1].x - points[0].x;
            int height = points[1].y - points[0].y;
            createRect(this.color, new Point(points[0]), width, height);
            countPoints = 0;
        }
    }

    private void checkCircleForCreating() {
        if (countPoints >= 2) {
            int a = points[1].x - points[0].x;
            int b = points[1].y - points[0].y;
            float radius = (float) Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));
            createCircle(this.color, new Point(points[0]), radius);
            countPoints = 0;
        }
    }

    private void checkTriangleForCreating() {
        if (countPoints >= 3) {
            createTriangle(this.color, new Point(points[0]), new Point(points[1]), new Point(points[2]));
            countPoints = 0;
        }
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public void setTypeShape(String type) {
        this.typeShape = type;
        countPoints = 0;
        invalidate();
    }
    public void deleteLast(){
        this.shapesCount -= 1;
        invalidate();
    }

    public void setColor(String color) {
        this.color = color;
    }
}
