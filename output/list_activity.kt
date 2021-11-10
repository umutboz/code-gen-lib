package com.myapp

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.RecyclerView

class ListActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val cities = listOf("Istanbul", "Ankara", "Izmir", "Mugla", "Ardagan")
        val adapter = CityAdapter(cities)

        val recyclerView = findViewById<RecyclerView>(R.id.recycler)
        recyclerView.adapter = adapter
    }
}