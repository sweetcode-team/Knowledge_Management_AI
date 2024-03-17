import React from 'react';
import DocumentCard from '@/app/chatbot/components/document-card';

export interface MessageContentProps {
  text: string;
  onButtonClick: () => void;
  role: string;
}

const MessageContent: React.FC<MessageContentProps> = ({ text, onButtonClick, role }) => (
  <>
    <p>{text}</p>
    {role === 'agent' && <DocumentCard onButtonClick={onButtonClick} />}
  </>
);

export default MessageContent;
