package com.example.myapplication;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.Toast;

import java.util.LinkedList;

public class BookSlotActivity extends AppCompatActivity {

    public static String sport;
    public static int date;
    public static String timeSlot;
    public static String name;
    public static String Block;
    public static String Tower;
    public static String unitNumber;

    Boolean TT;
    Boolean badminton;

    Boolean slot1;
    Boolean slot2;
    Boolean slot3;
    Boolean slot4;
    Boolean slot5;
    Boolean slot6;
    Boolean slot7;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_book_slot);


        TT = false;
        badminton = false;

        slot1 = false;
        slot2 = false;
        slot3 = false;
        slot4 = false;
        slot5 = false;
        slot6 = false;
        slot7 = false;

    }

    public void setTT(View view){
        if (TT == false){
            TT = true;
        }
        else {
            TT = false;
        }
    }

    public void setBadminton(View view){
        if (badminton == false){
            badminton = true;
        }
        else {
            badminton = false;
        }
    }

    public void slot1(View view){
        if (slot1 == false){
            slot1 = true;
        }
        else {
            slot1 = false;
        }
    }

    public void slot2(View view){
        if (slot2 == false){
            slot2 = true;
        }
        else {
            slot2 = false;
        }
    }

    public void slot3(View view){
        if (slot3 == false){
            slot3 = true;
        }
        else {
            slot3 = false;
        }
    }

    public void slot4(View view){
        if (slot4 == false){
            slot4 = true;
        }
        else {
            slot4 = false;
        }
    }

    public void slot5(View view){
        if (slot5 == false){
            slot5 = true;
        }
        else {
            slot5 = false;
        }
    }

    public void slot6(View view){
        if (slot6 == false){
            slot6 = true;
        }
        else {
            slot6 = false;
        }
    }

    public void slot7(View view){
        if (slot7 == false){
            slot7 = true;
        }
        else {
            slot7 = false;
        }
    }

    public void setDetails(View view){
        EditText nameEnter = findViewById(R.id.name);
        name = nameEnter.getText().toString();

        DatePicker dateEnter = findViewById(R.id.date);
        date = dateEnter.getDayOfMonth();

        EditText blockEnter = findViewById(R.id.block);
        Block = blockEnter.getText().toString();
        EditText towerEnter = findViewById(R.id.tower);
        Tower = towerEnter.getText().toString();
        EditText unitNumberEnter = findViewById(R.id.unit_number);
        unitNumber = unitNumberEnter.getText().toString();

        if (TT == true){
            sport = "TT";
        }
        else{
            sport = "badminton";
        }

        if (slot1 == true){
            timeSlot = "9am -10 am";
        }
        else if (slot2 == true){
            timeSlot = "10am - 11am";
        }
        else if (slot3 == true){
            timeSlot = "11am - 12pm";
        }
        else if (slot4 == true){
            timeSlot = "4pm - 5pm";
        }
        else if (slot5 == true){
            timeSlot = "5pm - 6pm";
        }
        else if (slot6){
            timeSlot = "6pm - 7pm";
        }
        else{
            timeSlot = "7pm - 8pm";
        }

        Intent bookSlot = new Intent(this, com.example.myapplication.MainActivity.class);
        startActivity(bookSlot);
        Toast.makeText(getApplicationContext(), "Booking Complete", Toast.LENGTH_SHORT).show();
    }

}
