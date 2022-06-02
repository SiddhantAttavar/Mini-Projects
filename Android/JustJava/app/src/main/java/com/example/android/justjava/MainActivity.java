/**
 * IMPORTANT: Make sure you are using the correct package name. 
 * This example uses the package name:
 * package com.example.android.justjava
 * If you get an error when copying this code into Android studio, update it to match teh package name found
 * in the project's AndroidManifest.xml file.
 **/

package com.example.android.justjava;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;


/**
 * This app displays an order form to order coffee.
 */
public class MainActivity extends AppCompatActivity {

    int quantity = 0;
    int price = 0;
    String priceMessage = "";
    Boolean whippedCream = false;
    Boolean chocolate = false;
    String name = "";
    String cream = "No";
    String chocolateText = "No";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    /**
     * This method is called when whipped cream is selected
     */
    public void cream(View view) {
        if (whippedCream == true){
            cream = "No";
            whippedCream = false;
        }
        else {
            cream = "Yes";
            whippedCream = true;
        }
    }

    /**
     * This method is called when chocolate is selected
     */
    public void chocolate(View view) {
        if (chocolate == true){
            chocolateText = "No";
            chocolate = false;
        }
        else {
            chocolateText = "Yes";
            chocolate = true;
        }
    }

    /**
     * This method is called when name is entered
     */
    public void name(View view) {
        EditText nameEnter = (EditText) findViewById(R.id.name_edit_text_view);
        Button nameSend = (Button) findViewById(R.id.enterName_button);
        name = nameEnter.getText().toString();
        nameSend.setBackgroundColor(Color.GREEN);
    }

    /**
     * This method is called when + button is clicked.
     */
    public void increment(View view) {
        if (quantity < 100) {
            quantity = quantity + 1;
        }
        displayQuantity();
        calculatePrice();
        displayPrice();
    }

    /**
     * This method is called when - button is clicked.
     */
    public void decrement(View view) {
        if (quantity > 0) {
            quantity = quantity - 1;
        }
        displayQuantity();
        calculatePrice();
        displayPrice();
    }

    /**
     * This method is called when the order button is clicked.
     */
    public void submitOrder(View view) {
        calculatePrice();
        orderSummary();
        displayMessage();

        Intent orderSummary = new Intent(Intent.ACTION_SEND);
        orderSummary.setType("*/*");
        orderSummary.putExtra(Intent.EXTRA_EMAIL  , new String[]{"siddhantattavar12@gmail.com"});
        orderSummary.putExtra(Intent.EXTRA_SUBJECT, "JustJava Order");
        orderSummary.putExtra(Intent.EXTRA_TEXT   , priceMessage);

        if (orderSummary.resolveActivity(getPackageManager()) != null) {
            startActivity(orderSummary);
        }
        else {
            Toast.makeText(getApplicationContext(), "Email Failed", Toast.LENGTH_SHORT).show();
        }
    }

    private void calculatePrice(){
        price = quantity * 5;
        if(whippedCream == true) {
            price = price + (quantity * 1);
        }
        if(chocolate == true) {
            price = price + (quantity * 2);
        }
    }

    private void orderSummary(){
        priceMessage = "Name: " + name + "\nQuantity: " + quantity + "\nWhipped cream: " + cream + "\nChocolate: " + chocolateText + "\nTotal: $" + price + "\nThank you!";
    }

    /**
     * This method displays the given quantity value on the screen.
     */
    private void displayQuantity() {
        TextView quantityTextView = (TextView) findViewById(R.id.quantity_text_view);
        quantityTextView.setText("" + quantity);
    }

    /**
     * This method displays the given price on the screen.
     */
    private void displayPrice() {
        TextView orderSummaryTextView = (TextView) findViewById(R.id.order_summary_text_view);
        orderSummaryTextView.setText("$" + price);
    }

    /**
     * This method displays the given text on the screen.
     */
    private void displayMessage() {
        TextView orderSummaryTextView = (TextView) findViewById(R.id.order_summary_text_view);
        orderSummaryTextView.setText(priceMessage);
    }

}