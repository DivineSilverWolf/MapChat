//package org.example.controller;
//
//import org.example.dao.Message;
//import org.example.dao.User;
//import org.example.repo.MessageRepo;
//import org.example.repo.UserRepo;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.stereotype.Controller;
//import org.springframework.web.bind.annotation.PostMapping;
//import org.springframework.web.bind.annotation.RequestMapping;
//import org.springframework.web.bind.annotation.RequestParam;
//
//import java.text.DateFormat;
//import java.text.ParseException;
//import java.text.SimpleDateFormat;
//import java.util.Date;
//import java.util.Optional;
//
//@Controller
//@RequestMapping(path="/message")
//public class MessageController {
//    @Autowired
//    UserRepo userRepo;
//
//    @Autowired
//    MessageRepo messageRepo;
//
//    @PostMapping(path="/add")
//    public String addMessage(@RequestParam String username,
//                          @RequestParam String messageText,
//                          @RequestParam String timestamp) {
//
//        DateFormat formatter = new SimpleDateFormat("yy:MM:dd:hh:mm:ss");
//        Date date = null;
//        try {
//            date = formatter.parse(timestamp);
//        } catch (ParseException e) {
//            System.out.println("Invalid date");
//        }
//
//        Optional<User> user = userRepo.findById(username);
//        if (user.isEmpty()) return "no such user";
//
//        messageRepo.save(new Message(user.get(), messageText, date));
//
//        return "saved";
//    }
//
//    @PostMapping(path="/delete")
//    public String deleteMessage(@RequestParam Long id) {
//        messageRepo.deleteById(id);
//        return "deleted";
//    }
//}
