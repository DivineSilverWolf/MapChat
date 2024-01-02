//package org.example.dao;
//
//import lombok.AllArgsConstructor;
//import lombok.Getter;
//import lombok.NoArgsConstructor;
//import lombok.Setter;
//
//import javax.persistence.*;
//import java.util.HashSet;
//import java.util.Set;
//
//@AllArgsConstructor
//@NoArgsConstructor
//@Getter
//@Setter
//@Entity
//public class Chat {
//    @Id
//    @GeneratedValue(strategy =  GenerationType.AUTO)
//    Long id;
//    String chatName;
//    String chatType;
//
//    @OneToMany
//    @JoinColumn(name = "message_id")
//    Set<Message> messages = new HashSet<>();
//
//    public Chat(String chatName, String chatType) {
//        this.chatName = chatName;
//        this.chatType = chatType;
//    }
//
//    public Chat(String chatName, String chatType, Set<Message> u) {
//        this.chatName = chatName;
//        this.chatType = chatType;
//        this.messages = u;
//    }
//}