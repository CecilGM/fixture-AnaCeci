import React from 'react';
import Button from '@mui/material/Button';

const MyButton = ({ 
  variant = "contained", 
  color = "primary", 
  onClick, 
  label = "Click me",
  disabled = false,
  size = "medium",
  fullWidth = false
}) => {
  return (
    <Button
      variant={variant}
      color={color}
      onClick={onClick}
      disabled={disabled}
      size={size}
      fullWidth={fullWidth}
      sx={{
        borderRadius: 2,
        textTransform: 'none',
        fontWeight: 'bold',
        '&:hover': {
          transform: 'scale(1.02)',
          transition: 'transform 0.2s'
        }
      }}
    >
      {label}
    </Button>
  );
};

export default MyButton;