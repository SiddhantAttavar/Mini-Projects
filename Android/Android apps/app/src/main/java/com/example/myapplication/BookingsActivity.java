package com.example.myapplication;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

import com.example.myapplication.BookSlotActivity;

public class BookingsActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_bookings);

        String orderSummary = "Name: " + BookSlotActivity.name;
        orderSummary = orderSummary + "\nFlat Number: " + BookSlotActivity.Block + "-" + BookSlotActivity.Tower + "-" + BookSlotActivity.unitNumber;
        orderSummary = orderSummary + "\nSport: " + BookSlotActivity.sport;
        orderSummary = orderSummary + "\nDate: " + BookSlotActivity.date;
        orderSummary = orderSummary + "\nTime: " + BookSlotActivity.timeSlot;

        TextView orderDisplay = findViewById(R.id.display_order);
        orderDisplay.setText(orderSummary);
    }

}
