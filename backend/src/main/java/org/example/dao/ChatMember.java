//package org.example.dao;
//
//import jakarta.persistence.*;
//import lombok.AllArgsConstructor;
//import lombok.Getter;
//import lombok.NoArgsConstructor;
//import lombok.Setter;
//
//import java.util.List;
//
//@AllArgsConstructor
//@NoArgsConstructor
//@Getter
//@Setter
//public class ChatMember {
//    @Id
//    @GeneratedValue(strategy =  GenerationType.AUTO)
//    Long Id;
//
//    @OneToOne
//    @JoinColumn(name = "user_id")
//    User user;
//}