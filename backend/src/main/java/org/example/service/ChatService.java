//package org.example.service;
//
//import org.example.dao.Chat;
//import org.example.dao.User;
//import org.example.repo.ChatRepo;
//import org.springframework.beans.factory.annotation.Autowired;
//
//import java.util.Optional;
//import java.util.Set;
//import java.util.stream.Collectors;
//
//
//public class ChatService {
//    @Autowired
//    ChatRepo chatRepo;
//
//    @Autowired
//    UserService userService;
//
//    public void addChat(Chat chat) {
//        chatRepo.save(chat);
//    }
//
//    public void deleteChatById(Long id) {
//        chatRepo.deleteById(id);
//    }
//
////    public void updateChatType(Chat chat) {
////        Optional<Chat> chat = chatRepo.findById(chat);
////        if (user.isEmpty()) return;
////
////        userRepo.save(user.get());
////    }
//
////    public Set<User> getAllUsersByChatId(Long id) {
////        Optional<Chat> chat = chatRepo.findById(id);
////        if (chat.isEmpty()) return null;
////
////        Set<User> users = userService.getAllUsers();
////
////        return users.stream()
////                .filter(u -> u.getChats().contains(chat.get())).collect(Collectors.toSet());
////    }
//}
