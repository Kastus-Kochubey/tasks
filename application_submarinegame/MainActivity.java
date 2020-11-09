package com.example.application_submarinegame;

import android.content.pm.ActivityInfo;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.view.Display;

import androidx.appcompat.app.AppCompatActivity;

import java.util.Arrays;
import java.util.Random;

public class MainActivity extends AppCompatActivity {
    int displayWidth;
    int displayHeight;
    //    int cellWidth;
//    int cellHeight;
    int numberVertCells;
    int numberHorCells;
    float density;
    int cellSize = 40;
    float vertCellSize;
    float horCellSize;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
//        setContentView(R.layout.activity_main);
        CustomView view = new CustomView(getApplicationContext(), density);
        setContentView(view);
//        setContentView(CustomView);
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
        Display display = getWindowManager().getDefaultDisplay();

        displayWidth = display.getWidth();
        displayHeight = display.getHeight();

        DisplayMetrics metrics = new DisplayMetrics();
        density = metrics.density;
        numberHorCells = (displayWidth % cellSize == 0) ? displayWidth / cellSize - 1 : displayWidth / cellSize;
        numberVertCells = (displayHeight % cellSize == 0) ? displayHeight / cellSize - 1 : displayHeight / cellSize;
        vertCellSize = (float) displayWidth / numberVertCells;
        horCellSize = (float) displayHeight / numberHorCells;
        System.out.println(numberHorCells);
        System.out.println(numberVertCells);
       // float density = getResources().getDisplayMetrics().density плотность пикселей - исп для размера клеток и ширины линий

//        cellWidth = displayWidth;
//        cellHeight = displayHeight;


//        drawGrid();
    }



    protected void makeSubmarineCoords() {
        Random r = new Random();
//        r.nextInt((max - min) + 1) + min;
        int[][] fieldOfCells = new int[numberVertCells][numberHorCells];
        fieldOfCells[r.nextInt(numberVertCells)][r.nextInt(numberHorCells)] = 1;
        for (int i = 0; i < numberVertCells; i++) {
                System.out.println(Arrays.toString(fieldOfCells[i]));

        }
        }


    }

