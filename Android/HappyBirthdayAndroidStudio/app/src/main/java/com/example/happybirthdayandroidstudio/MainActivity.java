package com.example.happybirthdayandroidstudio;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void enterName(View view){
        /** To send the name */
    }

    public void openBooking(View view){
        setContentView(R.layout.activity_booking);
    }

}
