package org.example.controller;

import org.example.dao.Location;
import org.example.repo.LocationRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.sql.Time;

@Controller
@RequestMapping(path="/location")
public class LocationController {

    @Autowired
    LocationRepo repo;

    @PostMapping(path="/add")
    public String addLocation(@RequestParam Integer latitude,
                          @RequestParam Integer longitude,
                          @RequestParam Time timestamp) {
        repo.save(new Location(latitude, longitude, timestamp));
        return "saved";
    }

    @PostMapping(path="/delete")
    public String deleteLocation(@RequestParam Long id) {
        repo.deleteById(id);
        return "deleted";
    }
}
