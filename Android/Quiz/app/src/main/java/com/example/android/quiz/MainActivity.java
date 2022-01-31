package com.example.android.quiz;

import android.graphics.Color;
import android.os.CountDownTimer;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.CheckBox;
import android.widget.TextView;
import android.widget.Toast;

import org.w3c.dom.Text;

public class MainActivity extends AppCompatActivity {

    String question = "In Venice, the gondola is a type of...";
    String option1Text = "Boat";
    String option2Text = "Stringed Instrument";
    String option3Text = "Sweet";
    String option4Text = "Paper";
    Boolean option1 = false;
    Boolean option2 = false;
    Boolean option3 = false;
    Boolean option4 = false;
    int score = 0;
    int questionNumber = 1;
    int correct = 0;
    int wrong = 0;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        displayQuestion();
        displayOption1();
        displayOption2();
        displayOption3();
        displayOption4();
        displayScore();
        displayWrong();
        displayCorrect();
    }

    public void quizButton(View view) {
        quiz();
    }

    /**
     *This method runs the quiz and is called when the next question button is clicked
     */
    public void quiz() {

        CheckBox option1CheckBox = (CheckBox) findViewById(R.id.option1_text_view);
        CheckBox option2CheckBox = (CheckBox) findViewById(R.id.option2_text_view);
        CheckBox option3CheckBox = (CheckBox) findViewById(R.id.option3_text_view);
        CheckBox option4CheckBox = (CheckBox) findViewById(R.id.option4_text_view);

        if (questionNumber == 1){

            option1CheckBox.setChecked(false);
            option2CheckBox.setChecked(false);
            option3CheckBox.setChecked(false);
            option4CheckBox.setChecked(false);

            displayQuestion();
            displayOption1();
            displayOption2();
            displayOption3();
            displayOption4();

            if (option1 == true) {
                score = score + 1;
                correct = correct + 1;
                displayOption1();
                displayOption2();
                displayOption3();
                displayOption4();
                Toast correct = Toast.makeText(this, "You are correct! Well Done!", Toast.LENGTH_SHORT);
                correct.show();
            }
            else {
                wrong = wrong + 1;
                displayOption1();
                displayOption2();
                displayOption3();
                displayOption4();
                Toast wrong = Toast.makeText(this, "Sorry, you are incorrect! Better Luck next time.", Toast.LENGTH_SHORT);
                wrong.show();
            }

            displayScore();
            displayCorrect();
            displayWrong();

            questionNumber = 2;

            question = "In Ali Baba and the Forty Theives, what was Ali Baba's profession?";
            option1Text = "Milkman";
            option2Text = "Woodcutter";
            option3Text = "Goldsmith";
            option4Text = "Cobbler";

            displayQuestion();
            displayOption1();
            displayOption2();
            displayOption3();
            displayOption4();

            option1 = false;
            option2 = false;
            option3 = false;
            option4 = false;

            option1CheckBox.setTextColor(Color.rgb(0,0,0));
            option2CheckBox.setTextColor(Color.rgb(0,0,0));
            option3CheckBox.setTextColor(Color.rgb(0,0,0));
            option4CheckBox.setTextColor(Color.rgb(0,0,0));
        }

        else if (questionNumber == 2){

            option1CheckBox.setChecked(false);
            option2CheckBox.setChecked(false);
            option3CheckBox.setChecked(false);
            option4CheckBox.setChecked(false);

            displayQuestion();
            displayOption1();
            displayOption2();
            displayOption3();
            displayOption4();

            if (option2 == true) {
                score = score + 1;
                correct = correct + 1;
                displayOption1();
                displayOption2();
                displayOption3();
                displayOption4();
                Toast correct = Toast.makeText(this, "You are correct! Well Done!", Toast.LENGTH_SHORT);
                correct.show();
            }
            else {
                wrong = wrong + 1;
                displayOption1();
                displayOption2();
                displayOption3();
                displayOption4();
                Toast wrong = Toast.makeText(this, "Sorry, you are incorrect! Better Luck next time.", Toast.LENGTH_SHORT);
                wrong.show();
            }

            displayScore();
            displayCorrect();
            displayWrong();

            questionNumber = 3;

            question = "Which sport is the term \"Silly Point\" associated with?";
            option1Text = "Kho Kho";
            option2Text = "Football";
            option3Text = "Kabbadi";
            option4Text = "Cricket";

            displayQuestion();
            displayOption1();
            displayOption2();
            displayOption3();
            displayOption4();

            option1 = false;
            option2 = false;
            option3 = false;
            option4 = false;

            option1CheckBox.setTextColor(Color.rgb(0,0,0));
            option2CheckBox.setTextColor(Color.rgb(0,0,0));
            option3CheckBox.setTextColor(Color.rgb(0,0,0));
            option4CheckBox.setTextColor(Color.rgb(0,0,0));
        }

        else if (questionNumber == 3){

            option1CheckBox.setChecked(false);
            option2CheckBox.setChecked(false);
            option3CheckBox.setChecked(false);
            option4CheckBox.setChecked(false);

            displayQuestion();
            displayOption1();
            displayOption2();
            displayOption3();
            displayOption4();

            if (option4 == true) {
                score = score + 1;
                correct = correct + 1;
                displayOption1();
                displayOption2();
                displayOption3();
                displayOption4();
                Toast correct = Toast.makeText(this, "You are correct! Well Done!", Toast.LENGTH_SHORT);
                correct.show();
            }
            else {
                wrong = wrong + 1;
                displayOption1();
                displayOption2();
                displayOption3();
                displayOption4();
                Toast wrong = Toast.makeText(this, "Sorry, you are incorrect! Better Luck next time.", Toast.LENGTH_SHORT);
                wrong.show();
            }

            displayScore();
            displayCorrect();
            displayWrong();

            questionNumber = 4;

            question = "Which team has played the maximum number of ODI's till 2016";
            option1Text = "India";
            option2Text = "New Zealand";
            option3Text = "Pakistan";
            option4Text = "England";

            displayQuestion();
            displayOption1();
            displayOption2();
            displayOption3();
            displayOption4();

            option1 = false;
            option2 = false;
            option3 = false;
            option4 = false;

            option1CheckBox.setTextColor(Color.rgb(0,0,0));
            option2CheckBox.setTextColor(Color.rgb(0,0,0));
            option3CheckBox.setTextColor(Color.rgb(0,0,0));
            option4CheckBox.setTextColor(Color.rgb(0,0,0));
        }

        else if (questionNumber == 4){

            option1CheckBox.setChecked(false);
            option2CheckBox.setChecked(false);
            option3CheckBox.setChecked(false);
            option4CheckBox.setChecked(false);

            displayQuestion();
            displayOption1();
            displayOption2();
            displayOption3();
            displayOption4();

            if (option1 == true) {
                score = score + 1;
                correct = correct + 1;
                displayOption1();
                displayOption2();
                displayOption3();
                displayOption4();
                Toast correct = Toast.makeText(this, "You are correct! Well Done!", Toast.LENGTH_SHORT);
                correct.show();
            }
            else {
                wrong = wrong + 1;
                displayOption1();
                displayOption2();
                displayOption3();
                displayOption4();
                Toast wrong = Toast.makeText(this, "Sorry, you are incorrect! Better Luck next time.", Toast.LENGTH_SHORT);
                wrong.show();
            }

            displayScore();
            displayCorrect();
            displayWrong();

            questionNumber = 5;

            question = "In the human body, the primary function of which organ is to remove waste and excess water?";
            option1Text = "Heart";
            option2Text = "Liver";
            option3Text = "Kidney";
            option4Text = "Large Intestine";

            displayQuestion();
            displayOption1();
            displayOption2();
            displayOption3();
            displayOption4();

            option1 = false;
            option2 = false;
            option3 = false;
            option4 = false;

            option1CheckBox.setTextColor(Color.rgb(0,0,0));
            option2CheckBox.setTextColor(Color.rgb(0,0,0));
            option3CheckBox.setTextColor(Color.rgb(0,0,0));
            option4CheckBox.setTextColor(Color.rgb(0,0,0));
        }

        else if (questionNumber == 5){

            option1CheckBox.setChecked(false);
            option2CheckBox.setChecked(false);
            option3CheckBox.setChecked(false);
            option4CheckBox.setChecked(false);

            if (option3 == true) {
                score = score + 1;
                correct = correct + 1;
                displayOption1();
                displayOption2();
                displayOption3();
                displayOption4();
                Toast correct = Toast.makeText(this, "You are correct! Well Done!", Toast.LENGTH_SHORT);
                correct.show();
            }
            else {
                wrong = wrong + 1;
                displayOption1();
                displayOption2();
                displayOption3();
                displayOption4();
                Toast wrong = Toast.makeText(this, "Sorry, you are incorrect! Better Luck next time.", Toast.LENGTH_SHORT);
                wrong.show();
            }

            displayScore();
            displayCorrect();
            displayWrong();

            question = "QUIZ OVER! Your score is: " + score;
            option1Text = "";
            option2Text = "";
            option3Text = "";
            option4Text = "";

            displayQuestion();
            displayOption1();
            displayOption2();
            displayOption3();
            displayOption4();

            option1CheckBox.setTextColor(Color.rgb(0,0,0));
            option2CheckBox.setTextColor(Color.rgb(0,0,0));
            option3CheckBox.setTextColor(Color.rgb(0,0,0));
            option4CheckBox.setTextColor(Color.rgb(0,0,0));
        }
    }

    /**
     * This method is called when option 1 is clicked
     */
    public void option1(View view) {
        if (option2 == true) {}
        else if (option3 == true){}
        else if (option4 == true){}
        else if (option1 == true){
            option1 = false;
        }
        else{
            option1 = true;
        }
    }

    /**
     * This method is called when option 2 is clicked
     */
    public void option2(View view) {
        if (option1 == true) {}
        else if (option3 == true){}
        else if (option4 == true){}
        else if (option2 == true){
            option2 = false;
        }
        else{
            option2 = true;
        }
    }

    /**
     * This method is called when option 3 is clicked
     */
    public void option3(View view) {
        if (option1 == true){}
        else if (option2 == true){}
        else if (option4 == true){}
        else if (option3 == true){
            option3 = false;
        }
        else{
            option3 = true;
        }
    }

    /**
     * This method is called when option 4 is clicked
     */
    public void option4(View view) {
        if (option1 == true) {}
        else if (option2 == true){}
        else if (option3 == true){}
        else if (option4 == true){
            option4 = false;
        }
        else{
            option4 = true;
        }
    }

    /**
     * This method writes the text for the question
     */
    public void displayQuestion() {
        TextView questionTextView = (TextView) findViewById(R.id.question_text_view);
        questionTextView.setText(question);
        questionTextView.setTextColor(Color.rgb(0,0,0));
    }

    /**
     * This method writes the text for the first option
     */
    public void displayOption1() {
        TextView option1TextView = (TextView) findViewById(R.id.option1_text_view);
        option1TextView.setText(option1Text);

    }

    /**
     * This method writes the text for the second option
     */
    public void displayOption2() {
        TextView option2TextView = (TextView) findViewById(R.id.option2_text_view);
        option2TextView.setText(option2Text);
    }

    /**
     * This method writes the text for the third option
     */
    public void displayOption3() {
        TextView option3TextView = (TextView) findViewById(R.id.option3_text_view);
        option3TextView.setText(option3Text);
    }

    /**
     * This method writes the text for the fourth option
     */
    public void displayOption4() {
        TextView option4TextView = (TextView) findViewById(R.id.option4_text_view);
        option4TextView.setText(option4Text);
    }

    /**
     * This method writes the text for the score
     */
    public void displayScore() {
        TextView scoreTextView = (TextView) findViewById(R.id.score_text_view);
        scoreTextView.setText("" + score);
        scoreTextView.setTextColor(Color.rgb(0,0,0));
    }

    /**
     * This method writes the text for the wrong
     */
    public void displayCorrect() {
        TextView correctTextView = (TextView) findViewById(R.id.correct_text_view);
        correctTextView.setText("" + correct);
    }

    /**
     * This method writes the text for the correct
     */
    public void displayWrong() {
        TextView wrongTextView = (TextView) findViewById(R.id.wrong_text_view);
        wrongTextView.setText("" + wrong);
    }

}