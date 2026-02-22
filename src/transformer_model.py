import torch
import torch.nn as nn


class TransformerIDS(nn.Module):
    def __init__(self, input_dim, d_model=64, nhead=4, num_layers=2, num_classes=2):
        super(TransformerIDS, self).__init__()

        # Feature embedding
        self.embedding = nn.Linear(input_dim, d_model)

        # Transformer Encoder
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=128,
            dropout=0.1,
            batch_first=True
        )
        self.transformer_encoder = nn.TransformerEncoder(
            encoder_layer,
            num_layers=num_layers
        )

        # Classification layer
        self.classifier = nn.Linear(d_model, num_classes)

        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        """
        Forward pass
        x shape: (batch_size, feature_dim)
        """

        # Add sequence dimension
        x = x.unsqueeze(1)

        # Embedding
        x = self.embedding(x)

        # Transformer Encoder
        x = self.transformer_encoder(x)

        # Global average pooling
        x = x.mean(dim=1)

        # Classification
        out = self.classifier(x)
        return out
