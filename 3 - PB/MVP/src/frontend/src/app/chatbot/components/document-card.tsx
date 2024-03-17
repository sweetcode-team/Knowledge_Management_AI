import React from 'react';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { ArrowRight } from 'lucide-react';

interface DocumentCardProps {
  onButtonClick: () => void;
}

const DocumentCard: React.FC<DocumentCardProps> = ({ onButtonClick }) => (
  <div className="flex items-stretch justify-between p-4">
    <Card className="flex-grow flex items-center justify-center p-2 text-lg font-semibold h-16">
      <p>Titolo documento rilevante</p>
    </Card>
    <Button className="flex items-center justify-center ml-4 h-16" onClick={onButtonClick}>
      <span className="mr-2">Vedi</span>
      <ArrowRight size={16} />
    </Button>
  </div>
);

export default DocumentCard;
