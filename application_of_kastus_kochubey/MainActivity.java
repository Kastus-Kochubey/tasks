package com.example.application_of_kastus_kochubey;

import android.content.pm.ActivityInfo;
import android.os.Bundle;
import android.view.Display;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    int width;
    int height;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
//        setContentView(R.layout.activity_main);
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
        Display display = getWindowManager().getDefaultDisplay();
        this.width = display.getWidth();
        this.height = display.getHeight();
        int[][] fieldOfCells = new int[height/30][width/30];
    }

    protected void drawGrid() {
        // draw grid
        for (int x = 0; x < width / 30; x++) {
            for (int y = 0; y < height; y += height) {

            }
        }


        Button button = new Button(getApplicationContext());
        setContentView(button);
    }


    public void click(View v) {
        TextView text = findViewById(R.id.textView);


    }

}