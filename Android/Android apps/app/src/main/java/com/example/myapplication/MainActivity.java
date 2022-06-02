package com.example.myapplication;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void openBookSlot(View view){
        Intent bookSlot = new Intent(this, com.example.myapplication.BookSlotActivity.class);
        startActivity(bookSlot);
    }

    public void openBookings(View view){
        Intent bookSlot = new Intent(this, com.example.myapplication.BookingsActivity.class);
        startActivity(bookSlot);
    }
}
