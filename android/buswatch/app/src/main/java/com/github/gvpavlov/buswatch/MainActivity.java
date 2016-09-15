package com.github.gvpavlov.buswatch;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.KeyEvent;
import android.view.inputmethod.EditorInfo;
import android.widget.EditText;
import android.widget.TextView;

import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.AsyncHttpResponseHandler;

import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;

import cz.msebera.android.httpclient.Header;


public class MainActivity extends AppCompatActivity {

    EditText editTextBus;
    EditText editTextStop;

    String serverUrl = "http://hoth:8080";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setResources();
        setListeners();
    }

    private void setResources() {
        editTextBus = (EditText) findViewById(R.id.edit_text_bus);
        editTextStop = (EditText) findViewById(R.id.edit_text_stop);
    }

    private void setListeners() {
        editTextBus.setOnEditorActionListener(new TextView.OnEditorActionListener() {
            @Override
            public boolean onEditorAction(TextView v, int actionId, KeyEvent event) {
                if (actionId == EditorInfo.IME_NULL
                        && event.getAction() == KeyEvent.ACTION_DOWN) {
                    Log.i("info", "after enter: " + v.getText().toString());
                    try {
                        bullshit(v.getText().toString());
                    } catch (UnsupportedEncodingException e) {
                        Log.e("error", "while bullshitting", e);
                    }
                }
                return true;
            }
        });

        editTextStop.setOnEditorActionListener(new TextView.OnEditorActionListener() {
            @Override
            public boolean onEditorAction(TextView v, int actionId, KeyEvent event) {
                if (actionId == EditorInfo.IME_NULL
                        && event.getAction() == KeyEvent.ACTION_DOWN) {
                    Log.i("info", "after enter: " + v.getText().toString());
                    try {
                        bullshit(v.getText().toString());
                    } catch (UnsupportedEncodingException e) {
                        Log.e("error", "while bullshitting", e);
                    }
                }
                return true;
            }
        });
    }

    String parametersKeyAndStop(Integer key, String stop) throws UnsupportedEncodingException {
        return "/arrivals?key=" + URLEncoder.encode(key.toString(), "UTF-8") + "&stop=" + URLEncoder.encode(stop, "UTF-8");
    }

    private void bullshit(String text) throws UnsupportedEncodingException {
        AsyncHttpClient client = new AsyncHttpClient();
        client.get(serverUrl + parametersKeyAndStop(42, text), new AsyncHttpResponseHandler() {

            @Override
            public void onStart() {
                // called before request is started
            }

            @Override
            public void onSuccess(int statusCode, Header[] headers, byte[] response) {
                String stringResponse = "";
                try {
                    stringResponse = new String(response, "UTF-8");
                } catch (Exception e) {
                    Log.i("error", "decode error ", e);
                }
                Log.i("info", "we've sent data " + stringResponse);
            }

            @Override
            public void onFailure(int statusCode, Header[] headers, byte[] errorResponse, Throwable e) {
                String stringResponse = "";
                try {
                    stringResponse = new String(errorResponse, "UTF-8");
                } catch (Exception e1) {
                    Log.i("error", "decode error ", e1);
                }
                Log.i("info", "neiiiiiin " + stringResponse);
            }

            @Override
            public void onRetry(int retryNo) {
                // called when request is retried
            }
        });
    }


    
}
