//package org.example.controller;
//
//import org.example.dao.Location;
//import org.example.repo.LocationRepo;
//import org.example.repo.UserRepo;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.stereotype.Controller;
//import org.springframework.web.bind.annotation.PostMapping;
//import org.springframework.web.bind.annotation.RequestMapping;
//import org.springframework.web.bind.annotation.RequestParam;
//
//import java.text.DateFormat;
//import java.text.ParseException;
//
//import java.text.SimpleDateFormat;
//import java.util.Date;
//
//@Controller
//@RequestMapping("/api/v1/location")
//public class LocationController {
//    @Autowired
//    LocationRepo locationRepo;
//
//    @Autowired
//    UserRepo userRepo;
//
//    @PostMapping("/locations")
//    public String addLocation(@RequestParam("username") String username,
//                          @RequestParam("latitude") Integer latitude,
//                          @RequestParam("latitude") Integer longitude,
//                          @RequestParam("timestamp") String timestamp) {
//
//        DateFormat formatter = new SimpleDateFormat("yy:MM:dd:hh:mm:ss");
//        Date date = null;
//
//        try {
//            date = formatter.parse(timestamp);
//        } catch (ParseException e) {
//            System.out.println("Invalid date");
//        }
//
//        var user = userRepo.findById(username);
//
//        locationRepo.save(new Location(latitude, longitude, date));
//        return "saved";
//    }
//}
