//package org.example.controller;

//import org.example.dao.Chat;
//import org.example.dao.User;
//import org.example.repo.ChatRepo;
//import org.example.repo.UserRepo;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.stereotype.Controller;
//import org.springframework.web.bind.annotation.PathVariable;
//import org.springframework.web.bind.annotation.PostMapping;
//import org.springframework.web.bind.annotation.RequestMapping;
//import org.springframework.web.bind.annotation.RequestParam;
//
//import java.util.Arrays;
//import java.util.HashSet;
//import java.util.Set;
//
//@Controller
//@RequestMapping(path="/")
//public class ChatController {
////    @Autowired
////    ChatRepo repo;
////
////    @Autowired
////    UserRepo userRepo;
//
//    @PostMapping(path="/chats")
//    public String addChat(@RequestParam String chatName,
//                          @RequestParam String chatType,
//                          @RequestParam String[] usernames) {
//
//
//
//
////        Set<User> u = (HashSet<User>) userRepo.findAllById(Arrays.asList(usernames));
////
////        repo.save(new Chat(chatName, chatType, null));
////        return "saved";
//    }
//
//    @PostMapping(path="/chats/{id}")
//    public String deleteChatById(@PathVariable("id") Long id) {
//        repo.deleteById(id);
//        return "deleted";
//    }
//}
//
//



