package com.example.application_submarinegame;

import android.content.pm.ActivityInfo;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.view.Display;

import androidx.appcompat.app.AppCompatActivity;

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
    static int cellX;
    static int cellY;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        DisplayMetrics metrics = new DisplayMetrics();
        density = metrics.density;
        System.out.println(density);
        CustomView view = new CustomView(getApplicationContext(), density);

        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
        Display display = getWindowManager().getDefaultDisplay();

        displayWidth = display.getWidth();
        displayHeight = display.getHeight();


        numberHorCells = displayWidth / cellSize;
        numberVertCells = displayHeight / cellSize;
        vertCellSize = (float) displayWidth / numberVertCells;
        horCellSize = (float) displayHeight / numberHorCells;
        makeSubmarineCoords();

        // float density = getResources().getDisplayMetrics().density плотность пикселей - исп для размера клеток и ширины линий
        setContentView(view);
    }



    protected void makeSubmarineCoords() {
        Random r = new Random();
        int[][] fieldOfCells = new int[numberVertCells][numberHorCells];
        int posX = r.nextInt(numberVertCells), posY = r.nextInt(numberHorCells);

    }


}

