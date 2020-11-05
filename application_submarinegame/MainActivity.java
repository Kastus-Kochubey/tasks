package com.example.application_submarinegame;

import android.content.pm.ActivityInfo;
import android.os.Bundle;
import android.view.Display;

import androidx.appcompat.app.AppCompatActivity;

import java.util.Random;

public class MainActivity extends AppCompatActivity {
    int displayWidth;
    int displayHeight;
    //    int cellWidth;
//    int cellHeight;
    int cellsVertNumber;
    int cellsHorNumber;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
//        setContentView(R.layout.activity_main);
        CustomView view = new CustomView(getApplicationContext());
        setContentView(view);
//        setContentView(CustomView);
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
        Display display = getWindowManager().getDefaultDisplay();

        displayWidth = display.getWidth();
        displayHeight = display.getHeight();

        cellsHorNumber = (displayWidth % 30 == 0) ? displayWidth / 30 - 1 : displayWidth / 30;
        cellsVertNumber = (displayHeight % 30 == 0) ? displayHeight / 30 - 1 : displayHeight / 30;
       // float density = getResources().getDisplayMetrics().density плотность пикселей - исп для размера клеток и ширины линий

//        cellWidth = displayWidth;
//        cellHeight = displayHeight;


    }

    protected void drawGrid() {
        // draw grid
        Random r = new Random();
//        r.nextInt((max - min) + 1) + min;
        int[][] fieldOfCells = new int[cellsVertNumber][cellsHorNumber];
        fieldOfCells[r.nextInt(cellsVertNumber)][r.nextInt(cellsHorNumber)] = 1;


//        setContentView(CustomView);

    }


//    public void click(View v) {
//        TextView text = findViewById(R.id.textView);
//
//
//    }

}