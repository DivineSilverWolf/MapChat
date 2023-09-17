package org.example.dao;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.util.List;
import java.util.Set;

@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
public class Chat {
    @Id
    @GeneratedValue(strategy =  GenerationType.AUTO)
    Long id;
    String chatName;
    String chatType;

    @OneToMany
    @JoinColumn(name = "message_id")
    Set<Message> messages;

    public Chat(String chatName, String chatType) {
        this.chatName = chatName;
        this.chatType = chatType;
    }

}